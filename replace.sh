docker rm -f wiktionary-definition;
docker rmi alaverydev/audio-language-wiktionary-definition;
docker build -t alaverydev/audio-language-wiktionary-definition .
docker push alaverydev/audio-language-wiktionary-definition