def calculate_total_cost(items: dict) -> float:
    """
    Calculate total cost of items.
    
    Args:
        items (dict): A dictionary containing item names and their quantities.
        
    Returns:
        float: The total cost of the items.
    """
    return sum(items.values())
