import streamlit as st
import openai
import os

openai.api_key = "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"

def generate_code(input_string):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_string +"\n",
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        temperature=0.0,
        stop=None,
    )
    answer = response.choices[0].text.strip()
    return answer.replace('\n', ' ')

def main():
    st.set_page_config(page_title="C++ Tutorial App")

    instructions = ['1. code for a factorial function',
                    '2. code to sort an array using bubble sort algorithm',
                    '3. code for a linked list data structure',
                    '4. code to read and write files in C++']

    str_inst = ''
    count = 0
    for i in instructions:
        str_inst = str_inst + i
        if count < len(instructions)-1:
            str_inst = str_inst + ',\n'
        count += 1

    input_string = "Generate C++ code for the following tasks:\n" + str_inst
    output = generate_code(input_string)

    print(f"Input: {input_string}\nOutput:\n{output}")

    task = st.selectbox("Select task:", instructions)

    if st.button("Generate code"):
        output = generate_code(task)
        st.code(output, language="cpp")

if __name__ == "__main__":
    main()
