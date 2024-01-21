import os
from tavily import TavilyClient
import sys

def tavily_search(query, search_depth='basic', max_results=5, include_images=False, 
                  include_answer=False, include_raw_content=False, include_domains=None, exclude_domains=None):
    """
    Performs a search using the Tavily API with additional customization options.

    Args:
    query (str): The search query.
    search_depth (str, optional): The search depth ('basic' or 'advanced'). Defaults to 'basic'.
    max_results (int, optional): Maximum number of search results to return. Defaults to 5.
    include_images (bool, optional): Whether to include images in the response. Defaults to False.
    include_answer (bool, optional): Whether to include a short answer in the response. Defaults to False.
    include_raw_content (bool, optional): Whether to include raw content of search results. Defaults to False.
    include_domains (list, optional): Specific domains to include in the search. Defaults to None.
    exclude_domains (list, optional): Specific domains to exclude from the search. Defaults to None.

    Returns:
    dict or str: The search results or context based on the search type and parameters.
    """
    try:
        # Retrieve API key from environment variable
        api_key = os.getenv('TAVILY_API_KEY')
        if not api_key:
            raise ValueError("TAVILY_API_KEY environment variable not set")

        tavily = TavilyClient(api_key=api_key)
        
        # Perform the search with additional parameters
        response = tavily.search(query=query, search_depth=search_depth, max_results=max_results,
                                 include_images=include_images, include_answer=include_answer, 
                                 include_raw_content=include_raw_content, include_domains=include_domains, 
                                 exclude_domains=exclude_domains)
        
        # Handle response
        if 'results' in response:
            return response
        else:
            raise ValueError("Unexpected response format from Tavily API")
    
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        return None

# Example usage
#results = tavily_search("ces 2024", search_depth='advanced', include_images=True)
#print(results)