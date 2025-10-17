import React from 'react';

/**
 * GameEmbed Component (Tailwind CSS Version)
 *
 * Embeds the Life Maze pygame game in an iframe with Tailwind styling.
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
    <div className="max-w-[1600px] mx-auto p-5">
      <div className="text-center mb-5">
        <h1 className="text-3xl font-bold text-gray-800 mb-2.5">
          Journey of Life - Maze Game
        </h1>
        <p className="text-lg text-gray-600">
          Use arrow keys to navigate and collect traits!
        </p>
      </div>

      <div className="bg-black rounded-lg overflow-hidden shadow-lg">
        <iframe
          src={GAME_URL}
          title="Life Maze Game"
          className="block mx-auto max-w-full bg-black border-0 w-full h-[50vh] lg:w-[1600px] lg:h-[800px]"
          frameBorder="0"
          allowFullScreen
        />
      </div>
    </div>
  );
};

export default GameEmbed;
