const { renderMermaidDiagram } = require('beautiful-mermaid');
const fs = require('fs');

const mermaidCode = `graph LR
  Client[Client Application]
  Gateway[API Gateway]
  Auth[Auth Service]
  Order[Order Service]
  Payment[Payment Service]
  Queue[Message Queue]
  Cache[Cache Layer]
  DB[(Database)]

  Client -->|HTTP| Gateway
  Gateway -->|validate| Auth
  Gateway -->|route| Order
  Auth -->|token| Order
  Order -->|async| Queue
  Order -->|cache| Cache
  Order -->|persist| DB
  Queue -->|process| Payment
  Payment -->|store| DB
  Cache -->|reads| DB`;

renderMermaidDiagram(mermaidCode, 'svg')
  .then(svg => {
    fs.writeFileSync('/sessions/compassionate-relaxed-johnson/mnt/local_1d65ab41-ddcd-47c8-a600-5ec2733d6d83/outputs/tech-rd-final/examples/architecture-diagram-beautiful.svg', svg);
    console.log('SVG rendered successfully');
  })
  .catch(err => {
    console.error('Error rendering diagram:', err.message);
  });
