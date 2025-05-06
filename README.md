
<h1>Simple Keylogger with <a href="https://keylogger-two.vercel.app/">Remote Server</a></h1>

<blockquote>
  ⚠️ <strong>Disclaimer:</strong> This project is intended for **educational and ethical research** only. Unauthorized use of keyloggers is illegal and unethical & if You Use it unethically, I not take any Responsibility
</blockquote>

<h2>📌 What is a Keylogger?</h2>
<p>A keylogger (short for "keystroke logger") is a type of surveillance technology used to monitor and record each keystroke typed on a keyboard. It can be used legitimately for parental controls or user testing—but also has potential for misuse.</p>

<h2>🌐 Check Out Web Server</h2>
<a href="https://keylogger-two.vercel.app/">Keylogger</a>

---
<h3>Types of Keyloggers</h3>
<ul>
  <li><strong>Software-based:</strong> Programs that run in the background of an OS, capturing input.</li>
  <li><strong>Hardware-based:</strong> Physical devices plugged into a machine that intercept key presses.</li>
  <li><strong>Remote-based:</strong> Keyloggers that send logs to a remote server periodically.</li>
</ul>

<h2>🛠️ Project Overview</h2>

<ul>
  <li>Logs all keystrokes using <code>pynput</code> in Python.</li>
  <li>Sends logs to a remote server every 10 seconds.</li>
  <li>Each log includes a <strong>user ID</strong> to track data per user.</li>
  <li>Remote server is a Flask app connected to a <strong>MongoDB</strong> database.</li>
  <li>Provides a web interface to view logs per user.</li>
</ul>


<h2>🖼️ Web Interface</h2>
<h3>User Dashboard</h3>
<img src="./WebServer/static/UserDash.png" alt="User Dashboard"></img>
<h3>User's Activity Logs</h3>
<img src="./WebServer/static/UserRec.png" alt="User's Activity Log"></img>


<h2>📦 How to Run Locally</h2>

<h3>Keylogger Client</h3>
<pre><code>pip install pynput requests
python keylogger.py</code></pre>
<p>Change the IP for Your Remote server & User Data.</p>

<h3>Flask Web Server</h3>
<pre><code>pip install flask pymongo
python app.py</code></pre>
<p>Change The Mongodb Server To Your server.</p>

<h2>🌐 Deploying to Remote Server</h2>
<p>To run this remotely, you can use services like Heroku, Render, or your own VPS.</p>

<h3>Steps:</h3>
<ol>
  <li>Set up a Linux server (e.g., Ubuntu).</li>
  <li>Install Python, Flask, and MongoDB client tools.</li>
  <li>Export your production MongoDB URI:
    <pre><code>export MONGO_URI="mongodb+srv://username:password@cluster.mongodb.net/keylogger"</code></pre>
  </li>
  <li>Run your app with:
    <pre><code>ngrok http 8000</code></pre>
  </li>
</ol>

<h2>🤝 Contributing</h2>
<p>We welcome contributions! To contribute:</p>
<ol>
  <li>Fork the repository</li>
  <li>Create your feature branch: <code>git checkout -b feature/your-feature</code></li>
  <li>Commit your changes: <code>git commit -m 'Add some feature'</code></li>
  <li>Push to the branch: <code>git push origin feature/your-feature</code></li>
  <li>Open a pull request</li>
</ol>

<h2>📝 License</h2>
<p>This project is licensed under the <strong><a href="https://github.com/ItsJESH/keyLogger?tab=MIT-1-ov-file">MIT License</a></strong>. You are free to use, modify, and distribute with attribution.</p>

<h2>📇 Author & Contact</h2>
<ul>
  <li><strong>GitHub:</strong> <a href="https://github.com/ItsJesh">ItsJesh</a></li>
  <li><strong>Email:</strong> <a href="mailto:jenishpaghadalin018@gmail.com">jenishpaghadalin018@gmail.com</a></li>
  <li><strong>X (Twitter):</strong> <a href="https://x.com/_je5h">@_je5h</a></li>
  <li><strong>Linkedin:</strong> <a href="https://www.linkedin.com/in/jenish-paghadal-391a17259/">Jenish Paghadal</a></li>
  <li><strong>Instagram:</strong> <a href="https://instagram.com/jenish.1911">@jenish.1911</a></li>
</ul>
