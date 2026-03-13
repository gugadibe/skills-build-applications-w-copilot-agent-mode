import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const apiUrl = codespace
    ? `https://${codespace}-8000.app.github.dev/api/activities/`
    : 'http://localhost:8000/api/activities/';

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Fetched activities:', results);
        console.log('API endpoint:', apiUrl);
      })
      .catch(err => console.error('Erro ao buscar atividades:', err));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2>Atividades</h2>
      <ul className="list-group">
        {activities.map((a, idx) => (
          <li key={a.id || idx} className="list-group-item">
            {a.type} - {a.duration} min - {a.date}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Activities;
