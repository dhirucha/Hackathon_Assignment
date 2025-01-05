# Social Media Performance Analysis Insights Tool  

This project is a no-code solution built using LangFlow, Python, and Streamlit to provide insights into social media engagement metrics. The application uses Astra DB for data storage and Groq AI for generating actionable insights.  

## About the Project  
This application was developed as a **Pre-Hackathon Assignment** by Team **TechTea**. It demonstrates the potential of combining no-code tools and APIs for solving real-world problems.  

## Features  
- **No-Code Components:** Built using LangFlow.  
- **User Interface:** Developed using Python and Streamlit for a seamless user experience.  
- **Data Storage:** Integration with Astra DB for managing engagement data.  
- **Insights Generation:** Powered by Groq AI to deliver actionable insights based on user input.  

## Application Flow  
1. **Chat Input Component:** Accepts the user’s post type input.  
2. **Prompt Component:** Prepares the query based on the input.  
3. **Astra DB Tool Component:** Fetches average engagement metrics (likes, shares, comments) for the each post type from the database.  
4. **Groq AI Agent Component:** Processes the metrics and generates actionable insights using the Groq AI API key.  
5. **Chat Output Component:** Displays the insights to the user in a conversational format.  

## Technologies Used  
- **LangFlow:** For application flow design using no-code components.  
- **Python:** For backend logic and integration.  
- **Streamlit:** For building the user interface.  
- **Astra DB:** For storing and querying engagement metrics.  
- **Groq AI API:** For generating insights.  

## Deployment  
The application has been deployed and is accessible via the following link:  
[Social Media Engagement Insights Tool](https://techtea-social-media-performance-analysis-insights-tool.streamlit.app/)  

## Team  
- **Team Name:** TechTea  
- **Members:**  
  - **Ruturaj Shinde** [GitHub](https://github.com/ruturaj1011)  
  - **Dheeraj Chaubey** [GitHub](https://github.com/dhirucha)  
  - **Tejas Narwade** [GitHub](https://github.com/TejasNarwade)

## Usage Instructions  
1. Access the deployed application using the link provided above.  
2. Enter the post type (e.g., carousel, reels, static images) into the chat input field.  
3. The tool will process your input, query the Astra DB, and generate insights using Groq AI.  
4. View the generated insights in the chat output section. 

## Environment Setup  
To run the project locally, create a `.env` file and add your **LangFlow Application Token** in the following format:  
```plaintext  
APPLICATION_TOKEN=your_application_token_here 
```


## Example Insights  

### Input  
Post type: `reels`  

### Output  
- "Reels have significantly higher shares but fewer comments compared to carousel posts."  
- "To increase likes on reels, consider using trending music and engaging captions."  
- "Reels outperform static images in every engagement metric."  

## How It Works  
- **LangFlow:** Manages the application flow using no-code components.  
- **Streamlit:** Provides an intuitive and interactive interface for users.  
- **Astra DB Tool:** Fetches real-time data about post types from the database.  
- **Groq AI:** Generates insights based on user-provided input and data.  

## Future Scope  
- Expand the database with more post types and engagement metrics.  
- Enhance UI to support additional visualizations like charts and graphs.  
- Implement user authentication for a more personalized experience.  


## Contact  
For questions or feedback, please contact:  
- **Ruturaj Shinde**: [ruturajnshinde1011@gmail.com](mailto:ruturajnshinde@gmail.com)  
- **Dheeraj Chaubey**: [dheerajubecha@gmail.com](mailto:dheerajubecha@gmail.com)  
- **Tejas Narwade**: [tejasnarwade2k5@gmail.com](mailto:tejasnarwade2k5@gmail.com)  
