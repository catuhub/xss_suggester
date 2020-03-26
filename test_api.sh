base="http://localhost:5000/wapt"

echo "Set hacking goal"
curl ${base}"/detection/xss"
# echo "Available observations"
# curl ${base}"/ask/observations"

# echo "Available actions"
# curl ${base}"/ask/actions"


#curl   -X PUT ${base}"/tell/observation/fHx8Tm9FcnJvcnN8fHx8fHxQZXJmZWN0UmVmbGVjdGlvbnx8fHx8fFJlcVZhbGlkfHx8fHx8U3RyaW5nUmVmbGVjdGVkSW5GdW5jdGlvbkJldHdlZW5RdW90ZXN8fHx8fHw="
curl   -X PUT ${base}"/tell/observation/fHx8Tm9FcnJvcnN8fHx8fHxQZXJmZWN0UmVmbGVjdGlvbnx8fHx8fFJlcVZhbGlkfHx8fHx8U3RyaW5nSXNSZWZsZWN0ZWRJbkhUTUx8fHx8fHw="
