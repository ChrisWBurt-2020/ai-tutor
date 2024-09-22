// Practice.js
import React, { useState } from 'react';
import axios from 'axios';
import { Button, Container, Typography, Paper, TextField } from '@mui/material';
import { styled } from '@mui/system';
import { motion } from 'framer-motion';

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(3),
  marginBottom: theme.spacing(3),
}));

function Practice() {
  const [codeInput, setCodeInput] = useState('');
  const [feedback, setFeedback] = useState('');

  const handleCodeInput = (event) => {
    setCodeInput(event.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post('/api/evaluate_code', {
        code: codeInput,
        subject: 'Python', // or get from user
        topic: 'Loops', // or get from user
      });
      setFeedback(response.data.feedback);
    } catch (error) {
      console.error('Error evaluating code:', error);
      setFeedback('An error occurred while evaluating your code.');
    }
  };

  return (
    <Container maxWidth="md" component={motion.div} initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
      <Typography variant="h2" gutterBottom>
        Practice
      </Typography>

      <StyledPaper elevation={3}>
        <Typography variant="h5" gutterBottom>
          Enter your code
        </Typography>
        <TextField
          fullWidth
          multiline
          rows={10}
          variant="outlined"
          value={codeInput}
          onChange={handleCodeInput}
          placeholder="Enter your code here..."
          margin="normal"
        />
        <Button variant="contained" color="primary" onClick={handleSubmit}>
          Submit Code
        </Button>
        {feedback && (
          <Typography variant="body1" style={{ marginTop: '1rem' }}>
            Feedback: {feedback}
          </Typography>
        )}
      </StyledPaper>
    </Container>
  );
}

export default Practice;
