def analyze_prompt(prompt):
    zodziu_skaicius = len(prompt.split())
    return {
        "originalas": prompt,
        "zodziu_skaicius": zodziu_skaicius,
        "analize": "Promptas atrodo tinkamas." if zodziu_skaicius < 50 else "Promptas per ilgas."
    }
