// Home.js
import React from 'react';
import { Link } from 'react-router-dom';
import { Typography, Button, Container } from '@mui/material';
import { styled } from '@mui/system';
import { motion } from 'framer-motion';

const HomeContainer = styled(Container)(({ theme }) => ({
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  justifyContent: 'center',
  minHeight: '100vh',
  backgroundColor: '#f0f4f8',
  padding: theme.spacing(4),
}));

const Title = styled(Typography)(({ theme }) => ({
  fontSize: '3rem',
  color: '#2c3e50',
  marginBottom: theme.spacing(4),
  textAlign: 'center',
}));

const Subtitle = styled(Typography)(({ theme }) => ({
  fontSize: '1.2rem',
  color: '#34495e',
  marginBottom: theme.spacing(4),
  textAlign: 'center',
  maxWidth: 600,
}));

function Home() {
  return (
    <HomeContainer component={motion.div} initial={{ opacity: 0 }} animate={{ opacity: 1 }} maxWidth="md">
      <Title variant="h1">Welcome to AI Tutor</Title>
      <Subtitle>
        Embark on a personalized learning journey with our AI-powered tutoring system.
        Enhance your skills and knowledge at your own pace.
      </Subtitle>
      <Button variant="contained" color="primary" size="large" component={Link} to="/learn">
        Start Learning
      </Button>
    </HomeContainer>
  );
}

export default Home;
