# ChatGPT Project Adapter

Generate the Project Kit with the CLI, then import `PROJECT_INSTRUCTIONS.md` in ChatGPT Project Settings and add the selected source-map/project docs via the supported UI. The exported JSON/source map is an index, **not proof that the files were uploaded**. Do not assume a connector automatically syncs them.

## Source-of-truth strategy
The Git repo owns current project rules. The ChatGPT Project is a **version-stamped snapshot/cache** and conversation context. Keep a `SOURCE_MANIFEST.json` with exact EngineeringOS kit revision and source pointers/hashes when available. On updates, compare manifest, produce a delta and ask the owner to update/remove stale sources through actual controls. No silent update of project instructions.

## Minimal imported files
`PROJECT_INSTRUCTIONS.md`, `PROJECT_SOURCE_MAP.md`, `PROJECT_PROFILE.json`, `SOURCE_MANIFEST.json`; add relevant native repo docs or links where supported. Large historical transcripts are retrieved selectively, not shoved wholesale into startup context.

## Host capability boundaries
Some chats can only read files, others have connected GitHub, cloud browser or desktop; setup claims must match actual accessible tools. ChatGPT Project setup does not grant access to local Windows executables, private paths or other agent harnesses. Installation/host connection always needs explicit access/authorization.
