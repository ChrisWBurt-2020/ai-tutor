import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

const HomeContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f0f4f8;
  padding: 2rem;
`;

const Title = styled.h1`
  font-size: 3rem;
  color: #2c3e50;
  margin-bottom: 2rem;
  text-align: center;
`;

const Subtitle = styled.p`
  font-size: 1.2rem;
  color: #34495e;
  margin-bottom: 2rem;
  text-align: center;
  max-width: 600px;
`;

const StyledLink = styled(Link)`
  background-color: #3498db;
  color: white;
  padding: 1rem 2rem;
  border-radius: 5px;
  text-decoration: none;
  font-size: 1.2rem;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #2980b9;
  }
`;

function Home() {
  return (
    <HomeContainer>
      <Title>Welcome to AI Tutor</Title>
      <Subtitle>
        Embark on a personalized learning journey with our AI-powered tutoring system.
        Enhance your skills and knowledge at your own pace.
      </Subtitle>
      <StyledLink to="/learn">Start Learning</StyledLink>
    </HomeContainer>
  );
}

export default Home;
