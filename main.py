meme_dict = {
    "CRINGE" : "Qualcosa di eccezionalmente strano o imbarazzante",
    "LOL": "Una risposta comune a qualcosa di divertente",
}

parola = input("Inserisci una parola moderna di cui non sai il significato (usa tutte le lettere maiuscole): ")

if parola in meme_dict.keys():
    print(meme_dict[parola])
else:
    print("Non abbiamo ancora questa parola... ci stiamo lavorando!")
