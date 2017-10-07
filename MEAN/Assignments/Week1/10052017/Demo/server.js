const express = require("express")
const path = require("Path")

const app = express()

const PORT = 8000

app.set("views", path.join(__dirname, "./client/views"))
app.set("view engine", "ejs")

app.get("/", (request, response) =>
{
	console.log("GET request at '/'")
	response.send("<h1>You reached a thing!</h1><p>Feels good, right?</p>")
	response.render("index", {name: name})
})

app.listen(PORT, () =>
{
	console.log(`Listening on port ${PORT}`)
}