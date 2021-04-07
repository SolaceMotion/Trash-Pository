const readline = require("readline")

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

console.log(
  "-".repeat(36) + "\nWelcome to the number guessing game!\n" + "-".repeat(36)
)
rl.question("Choose min: ", chooseMin => {
  //Questions
  rl.question("Choose max: ", chooseMax => {
    const intMin = parseInt(chooseMin, 10) //Parse readline input from string to int
    const intMax = parseInt(chooseMax, 10)

    function guessingGame(min, max) {
      if (isNaN(min) || isNaN(max)) {
        throw new ReferenceError("Parameter must be of type 'number'")
      }

      const n = Math.floor(Math.random() * max) + min
      let attempts = 1

      rl.setPrompt(`Input an integer from ${min} through ${max}: `)
      console.log()
      rl.prompt()
      rl.on("line", guess => {
        if (guess < n) {
          console.log("--------\nToo low!\n--------")
          attempts += 1
          rl.prompt()
        } else if (guess > n) {
          console.log("--------\nToo high!\n--------")
          attempts += 1
          rl.prompt()
        } else if (guess == n) {
          console.log(
            `\nCongrats, the correct answer was ${n}. You guessed correctly after ${attempts} attempts!\n`
          )
          rl.close()
        } else if (typeof guess == "string") {
          console.log(
            "------------------------------\nGuess must be of type 'number'\n------------------------------"
          )
          rl.prompt()
        }
      })

      rl.on("SIGINT", () => {
        rl.question("Exit (y or n)", input => {
          if (input.match(/^y(es)?$/i)) {
            rl.pause()
          } else {
            rl.resume()
            console.log()
            rl.prompt()
          }
        })
      })
    }

    try {
      guessingGame(intMin, intMax) //Pass int as parameter
    } catch (error) {
      console.error(error)
      rl.close()
    }
  })
})
