import React from 'react';

/**
 * GameEmbed Component
 *
 * Embeds the Life Maze pygame game in an iframe.
 *
 * Usage in your React site:
 * 1. Copy this component to your React project (e.g., src/components/GameEmbed.jsx)
 * 2. Import and use it in any page:
 *    import GameEmbed from './components/GameEmbed';
 *    <GameEmbed />
 *
 * After deploying to GitHub Pages, replace GAME_URL with your actual URL:
 * https://YOUR_USERNAME.github.io/Life-Maze/
 */

const GameEmbed = () => {
  // Replace this with your actual GitHub Pages URL after deployment
  const GAME_URL = 'https://YOUR_USERNAME.github.io/Life-Maze/';

  return (
    <div className="game-container">
      <div className="game-header">
        <h1>Journey of Life - Maze Game</h1>
        <p>Use arrow keys to navigate and collect traits!</p>
      </div>

      <div className="game-wrapper">
        <iframe
          src={GAME_URL}
          title="Life Maze Game"
          width="1600"
          height="800"
          frameBorder="0"
          allowFullScreen
          style={{
            border: 'none',
            display: 'block',
            margin: '0 auto',
            maxWidth: '100%',
            backgroundColor: '#000'
          }}
        />
      </div>

      <style jsx>{`
        .game-container {
          max-width: 1600px;
          margin: 0 auto;
          padding: 20px;
          font-family: system-ui, -apple-system, sans-serif;
        }

        .game-header {
          text-align: center;
          margin-bottom: 20px;
        }

        .game-header h1 {
          color: #333;
          margin-bottom: 10px;
        }

        .game-header p {
          color: #666;
          font-size: 1.1em;
        }

        .game-wrapper {
          background: #000;
          border-radius: 8px;
          overflow: hidden;
          box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        @media (max-width: 1600px) {
          .game-wrapper iframe {
            width: 100%;
            height: 50vh;
          }
        }
      `}</style>
    </div>
  );
};

export default GameEmbed;
