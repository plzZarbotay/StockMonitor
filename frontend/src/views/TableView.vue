<template>
  <div class="container">
    <table>
      <thead>
        <tr>
          <th>Название</th>
          <th>Цена</th>
          <th>Изм. за день</th>
          <th>Капитализация</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ 1 }}</td>
          <td>{{ 1 }}</td>
          <td>{{ 1 }}</td>
          <td>{{ 1 }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style>
body {
  font-family: system-ui;
  color: white;
}

.container {
  display: flex;
  justify-content: center;
  text-align: center;
}

thead,
tfoot {
  font-size: large;
  color: #fff;
  border-bottom: 1px solid #fff;
}

table {
  position: absolute;
  width: 1284px;
  height: 868px;
  top: 52px;
  background: #335062;
  border-radius: 29px;
  border-collapse: collapse;
  font-family: sans-serif;
  font-size: 0.8rem;
  letter-spacing: 1px;
}

tbody {
  font-size: medium;
}

th,
td {
  padding: 8px 10px;
}

td {
  text-align: center;
}
</style>
