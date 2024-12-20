import streamlit as st
import numpy as np
import time

def main_page():

    st.title("Welcome to My Page")
    st.header("Programming languages")

    all_langs = ['python', 'Java', 'C#']

    selected_langs = st.selectbox(
        "Select Language Name", options=list(all_langs)
    )

    if "python"in selected_langs:

        st.write("""  Introduction to Python:
                 
            Python is a high-level, interpreted programming language known for its simplicity and readability.
            Created by Guido van Rossum and first released in 1991.
            Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
            """
        )
    elif "Java" in selected_langs:
        st.write( 
            """ Introduction to Java:

            Java is a high-level, object-oriented programming language developed by James Gosling at Sun Microsystems (now owned by Oracle) in 1995.
            It is designed to be platform-independent, meaning Java programs can run on any device with a Java Virtual Machine (JVM) — a concept referred to as Write Once, Run Anywhere (WORA).
            """
        )


    elif "C#" in selected_langs:
        st.header("Introduction to C:")
        st.write(
            """
            C is a general-purpose, procedural programming language developed by Dennis Ritchie at Bell Labs in 1972.
            It is one of the oldest and most widely used programming languages, serving as the foundation for many modern languages like C++, Java, and Python.
            """
        )
    else:
        "Thank You for visiting"

    st.sidebar.header("Select Language Option")

def python():
    import streamlit as st
    st.header("Python")
    st.write(
    """ Introduction to Python:

        Python is a high-level, interpreted programming language known for its simplicity and readability.
        Created by Guido van Rossum and first released in 1991.
        Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
        Introduction to Python:

        Python is a high-level, interpreted programming language known for its simplicity and readability.
        Created by Guido van Rossum and first released in 1991.
        Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
        Key Features of Python:

        Easy to Learn: Python’s syntax is clean and straightforward, making it beginner-friendly.
        Interpreted: Python code is executed line-by-line, which makes debugging easier.
        Dynamically Typed: You don't need to declare the type of variables (e.g., x = 5 automatically considers x as an integer).
        Extensive Libraries: Python has a wide range of standard libraries for tasks like web development, data analysis, machine learning, and more.
        Applications of Python:

        Web Development: Frameworks like Django and Flask are used to build websites.
        Data Science and Machine Learning: Libraries like NumPy, pandas, TensorFlow, and PyTorch.
        Automation: Python is widely used for scripting and automating repetitive tasks.
        Game Development: Libraries like Pygame are used for developing games.
        Scientific Computing: Tools like SciPy and matplotlib are used for simulations and data visualization.
        Basic Syntax Rules:
        
    """
    )
    
def Java():
    import streamlit as st
    st.header("Java")
    st.write(
        """Introduction to Java:

            Java is a high-level, object-oriented programming language designed to be platform-independent.
            It was developed by James Gosling at Sun Microsystems and first released in 1995.
            Java applications are compiled into bytecode, which can run on any device with a Java Virtual Machine (JVM), making it "Write Once, Run Anywhere" (WORA).
        Key Features of Java:

            Object-Oriented: Everything in Java revolves around objects and classes, promoting modular and reusable code.
            Platform-Independent: Bytecode generated by the Java compiler can run on any platform with a JVM.
            Robust and Secure: Java includes features like automatic memory management and garbage collection, reducing errors.
            Multi-threaded: Java supports multi-threading, enabling efficient execution of concurrent tasks.
            Portable: Java code is architecture-neutral and can run on various hardware configurations.
            Applications of Java:

            Web Development: Frameworks like Spring and Hibernate are widely used for developing web applications.
            Mobile Development: Java is a key language for developing Android applications.
            Enterprise Applications: Java powers large-scale enterprise applications using tools like Java EE.
                
        """
        )

def C():
    import streamlit as st
    st.header("C Programing")
    st.write(
        """1. Introduction to C:

        C is a general-purpose, procedural programming language developed by Dennis Ritchie at Bell Labs in 1972.
        It is one of the oldest and most widely used programming languages, serving as the foundation for many modern languages like C++, Java, and Python.

        2. Key Features of C:

        Structured Language: Programs are divided into functions, making the code easier to understand and debug.
        Low-Level Access: C provides direct access to memory using pointers, making it ideal for system-level programming.
        Portable: Code written in C can be executed on different platforms with minimal modifications.
        Rich Library Support: It provides a wide range of built-in functions to perform various tasks.
        Efficient: Programs written in C are fast and efficient due to its proximity to hardware.
        """
        )



page= {
    "Main": main_page,
    "Python": python,
    "Java": Java,
    "C Programming": C
}


Option = st.sidebar.selectbox("select option", page.keys())
page[Option]()

