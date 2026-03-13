import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const apiUrl = codespace
    ? `https://${codespace}-8000.app.github.dev/api/teams/`
    : 'http://localhost:8000/api/teams/';

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Fetched teams:', results);
        console.log('API endpoint:', apiUrl);
      })
      .catch(err => console.error('Erro ao buscar teams:', err));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2>Times</h2>
      <ul className="list-group">
        {teams.map((t, idx) => (
          <li key={t.id || idx} className="list-group-item">
            {t.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Teams;
