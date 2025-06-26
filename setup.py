from setuptools import setup, find_packages

setup(
    name='promptcrafter',
    version='0.1.0',
    description='A multi-agent LLM system for generating, testing, evaluating, and summarizing prompts.',
    author='Nihal Kumar',
    author_email='your_email@example.com',  # optional
    packages=find_packages(),
    install_requires=[
        'crewai',
        'crewai-tools',
        'langchain',
        'openai',       
        'pydantic',     
        'python-dotenv' 
        'transformer',
        'accelerate',
        'torch'
    ],
    entry_points={
        'console_scripts': [
            'promptcrafter=promptcrafter.main:main'
        ]
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.8',
)
