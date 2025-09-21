from mcp.server.fastmcp import FastMCP
from movies_reader import find_movies

mcp = FastMCP("Netflix Movie Finder", "1.0")

@mcp.prompt()
def find_movies_prompt(country: str, genre: str, year: int) -> list[str]:
    return f"Find good {genre} movies from {country} filmed in {year}."

@mcp.tool()
def find_movies_tool(country: str, genre: str, year: int) -> list[str]:
    results = find_movies([genre], country, year)
    return results['title'].tolist()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
    #print(find_movies_tool("United States Of America", "Comedy", 2025))
