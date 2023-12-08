import React from 'react';
import './Nav.css';

const Nav = () => {
  return (
    <nav className="navbar">
      <div className="container">
        <a className="logo" href="/">
          HackRush Team
        </a>
        <ul className="nav-list">
          <li className="nav-item">
            <a className="nav-link" href="/home">
              Home
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/solution">
              Solution
            </a>
          </li>
          
        </ul>
      </div>
    </nav>
  );
};

export default Nav;