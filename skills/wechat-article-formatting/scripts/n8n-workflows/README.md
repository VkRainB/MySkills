# n8n Workflows

These are starter workflows for the WeChat article automation.

## Import

1. Open n8n UI and import the JSON file.
2. Update credentials / API keys as needed.
3. Activate the workflow.

## Workflows

- image-upload.json: accepts an image payload and returns upload result.
- create-draft.json: accepts HTML content and returns draft creation result.

## Expected Payloads

Image upload (POST JSON):

```json
{
  "image": "<base64>",
  "filename": "cover.png",
  "type": "permanent"
}
```

Create draft (POST JSON):

```json
{
  "title": "Article title",
  "content": "<html>",
  "author": "",
  "digest": "",
  "thumb_media_id": "",
  "content_source_url": ""
}
```

Adjust nodes to call your WeChat Official Account API or your internal service.
