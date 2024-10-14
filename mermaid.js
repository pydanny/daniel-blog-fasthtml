import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';

mermaid.initialize({
    startOnLoad: false,
    theme: 'base',
    securityLevel: 'loose',
    flowchart: { useMaxWidth: false, useMaxHeight: false }
});

function renderMermaidDiagrams() {
    const diagrams = document.querySelectorAll('.language-mermaid');
    diagrams.forEach((element, index) => {
        try {
            const graphDefinition = element.textContent;
            const graphId = `mermaid-diagram-${index}`;
            mermaid.render(graphId, graphDefinition)
                .then(({svg, bindFunctions}) => {
                    element.innerHTML = svg;
                    bindFunctions?.(element);
                })
                .catch(error => {
                    console.error(`Error rendering Mermaid diagram ${index}:`, error);
                    element.innerHTML = `<p>Error rendering diagram: ${error.message}</p>`;
                });
        } catch (error) {
            console.error(`Error processing Mermaid diagram ${index}:`, error);
        }
    });
}

proc_htmx('.language-mermaid', () => {
    renderMermaidDiagrams()
    // setTimeout(renderMermaidDiagrams, 100);
});