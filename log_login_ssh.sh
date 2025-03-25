#!/bin/bash

# URL du webhook Discord
WEBHOOK_URL="https://discord.com/api/webhooks/mettrevotrewebhook"
# Utilisateur Discord à notifier
DISCORDUSER="@everyone"

# Capture uniquement les sessions ouvertes et fermées
case "$PAM_TYPE" in
    open_session)
        # Prépare le message pour l'ouverture de session
        PAYLOAD="{ \"content\": \"$DISCORDUSER: User \`$PAM_USER\` logged in to \`$HOSTNAME\` (remote host: $PAM_RHOST).\" }"
        ;;
    close_session)
        # Prépare le message pour la fermeture de session
        PAYLOAD="{ \"content\": \"$DISCORDUSER: User \`$PAM_USER\` logged out of \`$HOSTNAME\` (remote host: $PAM_RHOST).\" }"
        ;;
esac

# Si le payload existe, envoie le webhook
if [ -n "$PAYLOAD" ] ; then
    curl -X POST -H 'Content-Type: application/json' -d "$PAYLOAD" "$WEBHOOK_URL"
fi
