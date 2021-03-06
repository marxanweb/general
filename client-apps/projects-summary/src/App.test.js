/*
 * Copyright (c) 2020 Andrew Cottam.
 *
 * This file is part of marxanweb/general
 * (see https://github.com/marxanweb/general).
 *
 * License: European Union Public Licence V. 1.2, see https://opensource.org/licenses/EUPL-1.2
 */
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
});
