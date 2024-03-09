package ai.raisepet

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class RaisePetApplication

fun main(args: Array<String>) {
    runApplication<RaisePetApplication>(*args)
}
