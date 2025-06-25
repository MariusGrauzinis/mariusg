import requests

def get_user_text():
    print("Enter your text (--- to finish):")
    lines = []
    while True:
        line = input()
        if line.strip() == "---":
            break
        lines.append(line)
    return " ".join(lines)

def main():
    text = get_user_text()
    if not text:
        print("No text provided.")
        return

    response = requests.post("http://localhost:5000/analyze", json={"text": text})

    if response.status_code == 200:
        print("Analysis result:")
        print(response.json())
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    main()
