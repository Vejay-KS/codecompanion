import React from "react";
import CodeOptimizerFormUI from "./CodeOptimizer";
import CodeDebuggerFormUI from "./CodeDebugger";
import CodeReviewerFormUI from "./CodeReviewer";
import CommentGeneratorFormUI from "./CommentGenerator";

const HomePage = () => {
  const [activeSection, setActiveSection] = React.useState("code-optimiser");

  const handleSectionChange = (sectionName) => {
    setActiveSection(sectionName);
  };

  const renderSection = () => {
    switch (activeSection) {
      case "code-optimiser":
        return <CodeOptimizerFormUI/>;
      case "code-debugger":
        return <CodeDebuggerFormUI/>;
      case "code-reviewer":
        return <CodeReviewerFormUI/>;
      case "comment-generator":
        return <CommentGeneratorFormUI/>;
      default:
        return <div>No section selected</div>;
    }
  };

  return (
    <div>
      <h1>Code Companion</h1>
      <nav>
        <button onClick={() => handleSectionChange("code-optimiser")}>
          Code Optimiser
        </button>
        <button onClick={() => handleSectionChange("code-debugger")}>
          Code Debugger
        </button>
        <button onClick={() => handleSectionChange("code-reviewer")}>
          Code Reviewer
        </button>
        <button onClick={() => handleSectionChange("comment-generator")}>
          Comment Generator
        </button>
      </nav>
      <main>{renderSection()}</main>
    </div>
  );
};

const CodeOptimiser = () => {
  return <div>This is the Code Optimiser section</div>;
};

const CodeDebugger = () => {
  return <div>This is the Code Debugger section</div>;
};

const CodeReviewer = () => {
  return <div>This is the Code Reviewer section</div>;
};

const CommentGenerator = () => {
  return <div>This is the Comment Generator section</div>;
};

export default HomePage;