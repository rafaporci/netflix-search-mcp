from mcp.server.fastmcp import FastMCP
from movies_reader import find_movies

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def find_movies_tool(country: str, genre: str, year: int) -> list[str]:
    results = find_movies([genre], country, year)
    return results['title'].tolist()


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
    #print(find_movies_tool("United States Of America", "Comedy", 2025))
