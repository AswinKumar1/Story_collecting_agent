#!/usr/bin/env python3
"""
Direct test of story classification without MCP
This bypasses Claude Desktop and tests the functionality directly
"""

import asyncio
import os
import sys
from dotenv import load_dotenv

# Add the current directory to Python path
sys.path.insert(0, os.getcwd())

# Load environment variables
load_dotenv()

# Import the classes from main.py
try:
    from main import EnhancedSourceDiscovery, IntelligentScraper, LearningClassifier, ExcelManager
except ImportError as e:
    print(f"Error importing from main.py: {e}")
    print("Make sure main.py is in the current directory")
    sys.exit(1)

async def test_story_collection():
    """Test story collection and classification directly."""
    
    print("🚀 Testing Story Classification System...")
    
    # Check environment variables
    google_api_key = os.getenv("GOOGLE_API_KEY")
    google_search_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID") 
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    
    print(f"Google API Key: {'✅ Found' if google_api_key else '❌ Missing'}")
    print(f"Search Engine ID: {'✅ Found' if google_search_engine_id else '❌ Missing'}")
    print(f"OpenRouter Key: {'✅ Found' if openrouter_api_key else '❌ Missing'}")
    
    if not all([google_api_key, google_search_engine_id, openrouter_api_key]):
        print("\n❌ Missing API keys in .env file")
        print("Make sure your .env file contains:")
        print("GOOGLE_API_KEY=your_key_here")
        print("GOOGLE_SEARCH_ENGINE_ID=your_id_here") 
        print("OPENROUTER_API_KEY=your_key_here")
        return
    
    try:
        # Initialize components
        print("\n🔧 Initializing components...")
        source_discovery = EnhancedSourceDiscovery(google_api_key, google_search_engine_id)
        scraper = IntelligentScraper(openrouter_api_key, "anthropic/claude-3-haiku")
        classifier = LearningClassifier()
        excel_manager = ExcelManager("test_economics_usa.xlsx")
        
        # Test with a smaller number first
        topic = "modern day economics USA"
        max_stories = 3
        
        print(f"\n🔍 Searching for {max_stories} stories about: {topic}")
        urls = await source_discovery.search_stories(topic, max_stories * 2)
        
        print(f"Found {len(urls)} potential URLs:")
        for i, url in enumerate(urls[:5], 1):
            print(f"  {i}. {url}")
        
        if not urls:
            print("❌ No URLs found. Check your Google Search setup.")
            return
        
        # Scrape and classify stories
        print(f"\n📄 Processing stories...")
        stories = []
        classifications = []
        
        for i, url in enumerate(urls[:max_stories], 1):
            print(f"\n--- Processing Story {i}/{max_stories} ---")
            print(f"URL: {url}")
            
            try:
                story = await scraper.scrape_story(url, topic)
                if story:
                    print(f"✅ Scraped: {story.title[:80]}...")
                    print(f"   Content length: {len(story.content)} chars")
                    print(f"   Data elements: {story.data_elements}")
                    
                    classification = classifier.classify_story(story)
                    print(f"📊 Classification: {classification.primary_framework}")
                    print(f"🎯 Confidence: {classification.confidence:.3f}")
                    print(f"🔍 Needs review: {classification.needs_review}")
                    
                    stories.append(story)
                    classifications.append(classification)
                else:
                    print(f"❌ Failed to extract usable content")
                    
            except Exception as e:
                print(f"❌ Error processing {url}: {e}")
        
        # Save to Excel
        if stories:
            print(f"\n💾 Saving {len(stories)} stories to Excel...")
            excel_manager.save_stories_and_classifications(stories, classifications)
            print("✅ Saved to test_economics_usa.xlsx")
            
            # Summary
            print(f"\n📋 Final Summary:")
            print(f"Successfully processed: {len(stories)} stories")
            print(f"High confidence: {sum(1 for c in classifications if c.confidence >= 0.6)}")
            print(f"Need review: {sum(1 for c in classifications if c.needs_review)}")
            
            print(f"\nStory breakdown:")
            for i, (story, classification) in enumerate(zip(stories, classifications), 1):
                print(f"{i}. {story.title[:60]}...")
                print(f"   Framework: {classification.primary_framework}")
                print(f"   Confidence: {classification.confidence:.3f}")
                print()
        else:
            print("❌ No stories were successfully processed")
        
        print("🎉 Test completed!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Clean up
        if 'scraper' in locals():
            await scraper.close_session()

if __name__ == "__main__":
    print("Direct Story Classification Test")
    print("=" * 50)
    asyncio.run(test_story_collection())