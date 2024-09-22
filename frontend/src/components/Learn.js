import React, { useEffect, useState } from 'react';
import axios from 'axios';
// ... existing imports ...
import { Button, Container, Typography, Paper, TextField } from '@mui/material';
import { styled } from '@mui/system';

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(3),
  marginBottom: theme.spacing(3),
}));

function Learn() {
  const [lesson, setLesson] = useState({});
  const [userInput, setUserInput] = useState('');
  const [aiResponse, setAiResponse] = useState('');

  useEffect(() => {
    // Replace 'Python' and 'Introduction' with dynamic values as needed
    axios.get('/api/lessons/Python/Introduction')
      .then(response => {
        setLesson(response.data);
      })
      .catch(error => {
        console.error('Error fetching lesson:', error);
      });
  }, []);

  const handleUserInput = (event) => {
    setUserInput(event.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post('/api/openai', { prompt: userInput });
      setAiResponse(response.data.response);
    } catch (error) {
      console.error('Error fetching AI response:', error);
    }
  };

  return (
    <Container maxWidth="md">
      <Typography variant="h2" gutterBottom>
        {lesson.topic}
      </Typography>
      
      <StyledPaper elevation={3}>
        <Typography variant="body1">{lesson.content}</Typography>
      </StyledPaper>

      <StyledPaper elevation={3}>
        <Typography variant="h5" gutterBottom>
          Ask AI Assistant
        </Typography>
        <TextField
          fullWidth
          multiline
          rows={3}
          variant="outlined"
          value={userInput}
          onChange={handleUserInput}
          placeholder="Ask a question about the lesson..."
          margin="normal"
        />
        <Button variant="contained" color="primary" onClick={handleSubmit}>
          Submit
        </Button>
        {aiResponse && (
          <Typography variant="body1" style={{ marginTop: '1rem' }}>
            AI Response: {aiResponse}
          </Typography>
        )}
      </StyledPaper>
    </Container>
  );
}

export default Learn;
