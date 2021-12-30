import * as exercise from './exercise_model.mjs';
import express from 'express';
const app = express();

const PORT = 3000;

app.use(express.urlencoded({
    extended: true
}));

app.use(express.json())

app.post("/exercises", (req, res) => {
    console.log(req.body)
    exercise.createExercise(req.body.name, req.body.reps, req.body.weight, req.body.unit, req.body.date )
        .then(exercise => {
            res.status(201).json(exercise);
        })
        .catch(error => {
            console.error(error);
            res.status(500).json(error);
            
        });
});

app.get("/exercises", (req,res)=> {
    exercise.findExercise()
        .then(exercise => {
            res.status(200).json(exercise);
        })
        .catch(error => {
        console.log("error");
        res.status(500);
        })
})

app.put("/exercises/:id", (req,res)=> {
    exercise.replaceExercise(req.params.id, req.body.name, req.body.reps, req.body.weight, req.body.unit, req.body.date)
        .then(numUpdated => {
            if (numUpdated === 1) {
                res.json({ _id: req.params._id, name: req.body.name, reps: req.body.reps, weight: req.body.weight, unit: req.body.unit, date: req.body.date })
            } else {
                res.status(404).json({ Error: 'Resource not found' });
            }
        })
        .catch(error => {
            console.log("error");
            res.status(500).json(error);
        })
})

app.delete("/exercises/:id", (req,res)=>{
    exercise.deleteById(req.params.id)
        .then( deletedCount => {
            if(deletedCount === 1) {
            res.status(204).send();
            }
            else {
                res.status(404).json({ Error: 'Resource not found' });
        }})
        .catch(error => {
            console.log("error");
            res.status(500).json(error);
        })
})

app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}...`);
});

