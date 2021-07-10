const express = require('express')

const app = express()
app.use(
    express.urlencoded({
      extended: true
    })
  )
  
app.use(express.json())

app.post("/data", (req,res) => {
  
    try {
        
        console.log(req.body.message) 
        
        if (req.body.message == "badData") {
           return  res.status(500).json({"message":"badData"})
        }   
       
        return res.status(200).json({"message":"success"})
    } catch (err) {
        return res.status(500).json(err)
    }
})

const port = 888 
app.listen(port, () => {
    console.log(`Node is running on port ${port}`)
})