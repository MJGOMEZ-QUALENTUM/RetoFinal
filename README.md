<body style="font-family: Arial, sans-serif; background-color: #f5f5f5; color: #333; padding: 20px;">
  <div style="max-width: 800px; margin: 0 auto;">
    <h1 style="text-align: center; color: #333;">Entorno de Desarrollo</h1>
    <p>Para comenzar a desarrollar, primero clona este repositorio con el siguiente comando:</p>
    <pre style="background-color: #eee; padding: 10px;"><code>git clone <a href="https://github.com/MJGOMEZ-QUALENTUM/RetoFinal.git" style="color: #333;">https://github.com/MJGOMEZ-QUALENTUM/RetoFinal.git</a></code></pre>
    
    <p>Tienes un contenedor Docker para ejecutar la aplicación con una base de datos PostgreSQL. Puedes ejecutarlo con el siguiente comando:</p>
    <pre style="background-color: #eee; padding: 10px;"><code>docker-compose up -d</code></pre>
    
    <p>Si es la primera vez que lo ejecutas, recuerda después de levantarlo crear la base de datos con el siguiente comando:</p>
    <pre style="background-color: #eee; padding: 10px;"><code>docker-compose exec web python manage.py</code></pre>
    
    <p>Además, tienes una batería de tests que puedes ejecutar en el directorio <code>tests</code>, en el archivo <code>test.py</code>. Puedes ejecutarlo con el siguiente comando:</p>
    <pre style="background-color: #eee; padding: 10px;"><code>docker-compose exec web bash -c 'cd tests &amp;&amp; coverage run -m unittest discover -s . &amp;&amp; coverage report -m --fail-under=80'</code></pre>
    
    <p>¡Muy importante! Estos fallarán si no se cubre el 80% de las líneas de código.</p>
    
    <p>Si estás en Linux, tienes un archivo <code>Makefile</code> con comandos rápidos:</p>
    <ol>
      <li><code>make iniciar</code>: para levantar por primera vez el contenedor.</li>
      <li><code>make parar</code>: para parar el contenedor.</li>
      <li><code>make reanudar</code>: para volver a ejecutarlo.</li>
      <li><code>make detener</code>: para parar el contenedor y borrar sus volúmenes/datos de la base de datos. Si lo deseas volver a usar, tendrás que usar <code>make iniciar</code>.</li>
      <li><code>make testear</code>: para ejecutar los tests y ver la cobertura por si lo necesitas antes de hacer.</li>
    </ol>
    
    <p>Si estás seguro de los cambios pero no quieres hacerlos en producción (main), puedes hacerlo en otra rama, por ejemplo dev, al hacer el <code>git push</code> se ejecutarán un action con los tests para confirmar que todo está bien antes de que hagas el pull request a la main.</p>
  </div>
</body>
