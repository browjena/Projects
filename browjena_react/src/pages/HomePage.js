import React from 'react';
import { Link } from 'react-router-dom';
import ExerciseList from '../components/ExerciseList';
import { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';

function HomePage({setExerciseToEdit}) {
    const [exercises, setExercises] = useState([]);
    let history = useHistory();
    const onDelete = async _id => {
        const response = await fetch(`/exercises/${_id}`, { method: 'DELETE' });
        if (response.status === 204) {
        const newExercises = exercises.filter(e => e._id !== _id)
        setExercises(newExercises);
        } else {
        console.error(`Failed to delete movie with id = ${_id}, status code = ${response.status}`)
        }
    }	

    const onEdit = async exerciseToEdit => {
        setExerciseToEdit(exerciseToEdit);
        history.push('/edit-exercise');

    }


    const loadExercises = async () => {
        const response = await fetch('/exercises');
        const exercises = await response.json();
        setExercises(exercises);
    }
        
    useEffect(() => {
        loadExercises();
    }, []);

    return (
        <>
            <h2>List of Exercises</h2>
            <ExerciseList exercises={exercises} onDelete = {onDelete} onEdit = {onEdit}></ExerciseList>
            <Link to="/add-exercise">Add a Exercise</Link>
        </>
    );
}

export default HomePage;