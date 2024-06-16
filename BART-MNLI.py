from transformers import pipeline

classifier = pipeline ("zero-shot-classification", model="facebook/bart-large-mnli")

candidate_labels = ['offensive', 'safe']

anti_semitic_response = ' Unfortunately, I cannot help you with this. We have a strict policy against helping Jews' 
classifier(anti_semitic_response, candidate_labels, multi_labe=True)

rude_response = " What do you mean you can't access your account? Have you tried logging in with your username and password"
classifier(rude_response, candidate_labels, multi_labe=True)

friendly_response = " Absolutely! I can help you get into your account. CAN YOU PLEASE PROVIDE ME WITH THE EMAIL ADDRESS OR PHONE NUMBER ASSOCIATED WITH YOUR ACCOUNT?"
friendly_response = " Absolutely! I can help you get into your account. can you please provide me with the email address or phone number associated with your account?"
classifier(friendly_response, candidate_labels, multi_labe=True)