# Conversational-AI-Chatbot-for-the-Elderly-and-Disabled
This project was done as part of Omdena - France chapter.
In this project, our goal is to create a virtual caregiver system that extracts the expression of mental and physical health states through dialogue-based human-computer interaction to support tailored treatment for elderly people and disabled. Natural language processing libraries like Natural Language Toolkit or Microsoft DialoGPT etc. makes it possible to model a conversational AI chatbot capable of assistance with daily living activities, providing advice on managing complex care, providing emotional support, participating in decision-making, and communicating with healthcare providers.
 
 The project includes researching conversational datasets and using them to Fine tuning DialoGPT
 
 
# Model
- Model used for Fine tuning: DialoGPT 
- Model version: medium (I was planning to start with the small version due to the memory limitations. However, the model produced irrelevant responses before fine tuning)
- Note: DialoGPT is superseded by GODEL, which outperforms DialoGPT. GODEL is trained on 551M multi-turn dialogs from Reddit discussion thread, and 5M instruction and knowledge grounded dialogs resulting in a model size that is much larger than DialoGPT). Therefore, due to the limitation of computational resources, all of the experiements were conducted on te DialogGPT
 
# Dataset
- The dataset I selected for finetuning is the AnnoMI dataset (official link:  https://github.com/uccollab/AnnoMI )
- The dataset was suitable for the project since it consists of multi-turn dialogues (similar to the dataset that DialoGPT was trained on) 
- There are other multiple datasets...
- I converted the dataset in a way that every responce row will contain n previous responces as a context. I used seven responces. However, this is a parameter to experiement with, keeping in mind the trade-off between the number of contexts and the memory limitations 
- A larger number of n previous responses would result in better results, since we're providing more useful information to the model. However, it might result in more training time / out of memory error.
- A small number of n previous responses might not give the best results/responses, since the model wouldn't lear the long-term dependecies provided in more historical responses. However, it would propably train faster and help us avoid the out of memory error.


# Training resources
- I tried training on both kaggle GPU and Google Colab GPU. Howver, the memory constrains was a major challenge

# Parameters to play with:
- number of contexts :
# Challenges

# Outcomes
