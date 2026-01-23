


konsole -p tabtitle=csafsync  -e bash -c "uv run csafsync; exec bash" &
konsole -p tabtitle=assetsync -e bash -c "uv run assetsync; exec bash" &
konsole -p tabtitle=matcher   -e bash -c "uv run csaf_matcher; exec bash" &
