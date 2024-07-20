# GenAI & TogetherAI Integration

Welcome to the GenAI & TogetherAI Integration repository! This project demonstrates how to utilize the GenAI and TogetherAI APIs in a streamlined application. Follow the steps below to get started.

## Getting Started

### Access the App Online
You can access the running application directly at:
[Writerr on Streamlit](https://writerr.streamlit.app/)

### 1. Clone the Repository
Clone this repository to your local machine using:
```bash
git clone https://github.com/tinkvu/WriterAI.git
cd WriterAI
```

### 2. Get GenAI API Key
- Visit [Google AI Studio](https://ai.google.com) to get your GenAI API Key.
- Sign up or log in to obtain the key.

### 3. Get TogetherAI API Key
- Contact TogetherAI to receive your API key.
- Visit their [website](https://together.ai) or reach out to their support team for instructions.

### 4. Add API Keys
Add your API keys to a `.env` file in the root directory or directly in the `app.py` file.

#### Using a `.env` File
Create a `.env` file and add the following lines:
```dotenv
genaiAPI=your_genai_api_key
togetherApi=your_togetherai_api_key
```

#### Directly in `app.py`
Alternatively, you can hardcode the API keys into `app.py` (not recommended for production):
```python
genaiAPI = "your_genai_api_key"
togetherApi = "your_togetherai_api_key"
```

### 5. Install Requirements
Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

### 6. Run the Application
Start the Streamlit application with:
```bash
streamlit run app.py
```

### Happy Writing!

## Snapshots

Here are some snapshots of the application in action:

![Snapshot 1](https://github.com/user-attachments/assets/d28811a3-16b1-4bd2-9083-77f0e9417d4c)

![Snapshot 2](https://github.com/user-attachments/assets/e13718e5-1393-4ea9-b9b4-4ce600e72995)

![Snapshot 3](https://github.com/user-attachments/assets/7a4c9889-4c93-4bd9-826f-16143507fcdf)

## Contributing

We welcome contributions! If you'd like to contribute, please follow the standard GitHub workflow:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

For any questions or issues, feel free to open an issue on the [GitHub repository](https://github.com/your-username/your-repo-name/issues).

Happy coding! 🚀
