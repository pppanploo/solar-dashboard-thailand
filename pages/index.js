// pages/index.js
import { useState } from 'react';
import Head from 'next/head';

export default function Dashboard() {
  const [language, setLanguage] = useState('th');

  const text = {
    th: {
      title: ☀️ แดชบอร์ดพลังงานแสงอาทิตย์',
      subtitle: 'สถานะการผลิตพลังงาน ณ ปัจจุบัน',
      inverter: 'อินเวอร์เตอร์',
      power: 'กำลังไฟ (kW)',
      status: 'สถานะ',
      location: 'ตำแหน่ง',
      language: 'ภาษา'
    },
    en: {
      title: '☀️ Solar Energy Dashboard',
      subtitle: 'Current energy production status',
      inverter: 'Inverter',
      power: 'Power (kW)',
      status: 'Status',
      location: 'Location',
      language: 'Language'
    }
  };

  const sampleData = [
    { id: 1, name: 'Huawei 10kW', power: 9.8, status: 'online', location: 'เชียงใหม่' },
    { id: 2, name: 'Growatt 20kW', power: 18.4, status: 'offline', location: 'ขอนแก่น' },
    { id: 3, name: 'SOLID 50kW', power: 48.9, status: 'online', location: 'ภูเก็ต' }
  ];

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif', background: '#fffbe6' }}>
      <Head>
        <title>{text[language].title}</title>
      </Head>

      <div style={{ display: 'flex', justifyContent: 'space-between' }}>
        <h1 style={{ color: '#f57c00' }}>{text[language].title}</h1>
        <select value={language} onChange={e => setLanguage(e.target.value)}>
          <option value="th">🇹🇭 ภาษาไทย</option>
          <option value="en">🇬🇧 English</option>
        </select>
      </div>
      <h2>{text[language].subtitle}</h2>

      <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '1rem' }}>
        <thead>
          <tr style={{ background: '#ffe0b2' }}>
            <th>{text[language].inverter}</th>
            <th>{text[language].power}</th>
            <th>{text[language].status}</th>
            <th>{text[language].location}</th>
          </tr>
        </thead>
        <tbody>
          {sampleData.map((item) => (
            <tr key={item.id} style={{ textAlign: 'center', background: item.status === 'online' ? '#e8f5e9' : '#ffebee' }}>
              <td>{item.name}</td>
              <td>{item.power.toFixed(1)}</td>
              <td>{item.status === 'online' ? '🟢' : '🔴'}</td>
              <td>{item.location}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

