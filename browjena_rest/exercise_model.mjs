// Get the mongoose object
import mongoose from 'mongoose';

// Prepare to the database movies_db in the MongoDB server running locally on port 27017
mongoose.connect(
    'mongodb://localhost:27017/exercises_db',
    { useNewUrlParser: true }
);

// Connect to to the database
const db = mongoose.connection;

// The open event is called when the database connection successfully opens
db.once('open', () => {
    console.log('Successfully connected to MongoDB using Mongoose!');
});

// Tell mongoose to create indexes, which help with faster querying
mongoose.set('useCreateIndex', true);

/**
 * Define the schema
 */
const exerciseSchema = mongoose.Schema({
    name: { type: String, required: true },
    reps: { type: Number, required: true },
    weight: { type: Number, required: true },
    unit: { type: String, required: true },
    date: { type: String, required: true }
});


const Exercise = mongoose.model("Exercise", exerciseSchema);


const createExercise = async (name, reps, weight, unit, date) => {
    // Call the constructor to create an instance of the model class Movie
    const exercise = new Exercise({ name: name, reps: reps, weight: weight, unit: unit, date: date });
    // Call save to persist this object as a document in MongoDB
    return exercise.save();
}


const findExercise = async () => {
    const query = Exercise.find()
    return query.exec();
}

const findExerciseById = async (id) => {
    const query =  Exercise.find({_id: id})
    return query.exec();
}

const replaceExercise = async (_id, name, reps, weight, unit, date) => {
    const result = await Exercise.replaceOne({ _id: _id },
        { name: name, reps: reps, weight: weight, unit: unit, date: date });
    return result.nModified;
}



const deleteById = async (_id) => {
    const result = await Exercise.deleteOne({ _id: _id });
    return result.deletedCount;
}

export { createExercise, findExercise, findExerciseById, replaceExercise, deleteById};
