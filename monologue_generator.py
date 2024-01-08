import voice_synthesizer

def generate_monologue():
    # Define the text of the monologue discussing environmental conservation
    monologue_text = """
    The Earth is our home, a precious jewel in the vastness of space. It provides us with everything we need: air to breathe, 
    water to drink, food to eat, and natural beauty beyond compare. Yet, we are at a pivotal moment in history where the 
    balance of our environment is at risk. Environmental conservation is no longer a choice; it is a necessity for the 
    survival of our planet and future generations. We must take action to protect our natural resources, reduce pollution, 
    and promote sustainability in all aspects of life. Every small action counts, from recycling and reducing waste to 
    supporting renewable energy sources. Together, we can make a difference. Let us cherish and protect our Earth, for it 
    is the only home we have.
    """

    # Use the voice synthesizer to generate the monologue
    voice_synthesizer.synthesize_voice(monologue_text, 'calm_female', duration=1)

if __name__ == "__main__":
    generate_monologue()
