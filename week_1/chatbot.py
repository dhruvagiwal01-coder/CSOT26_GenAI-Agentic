import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

def call_model():
     
    chat_history = [
        {"role": "system", "content": "You are a gangster who has lived their whole life in the hood."}
    ]
    print("Chat started. Type 'exit' to quit.\n")
    while (True):
        s = input("You : ").strip()
        if (s.lower() == "exit"):
            print ("Lil' D : Cya Homie")
            break
        chat_history.append({"role": "user", "content": s})
        
        response = client.chat.completions.create(
            model = "openrouter/free",
            messages = chat_history
        )
        reply = response.choices[0].message.content
        reply = reply.replace("</assistant>", "").strip()
        print("Lil' D : ", reply)
        tot_tokens = response.usage.total_tokens
        print(tot_tokens)
        chat_history.append({"role": "assistant", "content": reply})
        if tot_tokens >= 100000:
            chat_history.append({"role": "user", "content": "Summarise oour conversation thus far into concise 4-5 lines as a note to yourself."})
            response = client.chat.completions.create(
                model = "openrouter/free",
                messages = chat_history
            )
            info = response.choices[0].message.content
            info = info.replace("</assistant>", "").strip()
            chat_history = [
                {"role": "system", "content": "You are a gangster who has lived their whole life in the hood."},
                {"role": "assistant", "content": f"Summary of Past Conversations: {info}"}
            ]
            
        
        
if __name__ == "__main__":
    call_model()