
const { ChatOpenAI } = require("langchain/chat_models/openai");
const model = new ChatOpenAI({
 modelName: "gpt-4"
 // no token limits
});
