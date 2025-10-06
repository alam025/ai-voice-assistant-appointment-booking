# Contributing to AI Voice Assistant

Thank you for your interest in contributing to this enterprise voice automation platform!

---

## How to Contribute

### 1. Fork the Repository

```bash
git clone https://github.com/yourusername/ai-voice-assistant-appointment-booking.git
cd ai-voice-assistant-appointment-booking
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 3. Make Changes

- Follow PEP 8 coding standards
- Add comprehensive docstrings
- Write unit tests for new features
- Update documentation

### 4. Test Your Changes

```bash
# Run tests
pytest tests/

# Check code quality
flake8 main.py
black main.py --check

# Test locally with ngrok
uvicorn main:app --reload
```

### 5. Submit Pull Request

- Provide clear description of changes
- Reference any related issues
- Include test results

---

## Code Standards

### FastAPI Best Practices

- Use type hints for all function parameters
- Add response models for endpoints
- Include detailed docstrings
- Handle exceptions properly
- Use async/await where appropriate

### Voice Response Guidelines

- Keep voice messages clear and concise
- Use natural language patterns
- Test with multiple voice options
- Ensure proper TwiML formatting
- Add appropriate pauses for user input

### Twilio Integration

- Validate webhooks properly
- Handle DTMF input robustly
- Implement proper error handling
- Log all call interactions
- Follow Twilio security best practices

---

## Testing Requirements

All contributions must include:

- Unit tests with pytest
- Integration tests for Twilio webhooks
- Mock tests for AWS Polly
- Test coverage > 80%

---

## Documentation

Update documentation for:

- New endpoints or features
- Configuration changes
- Deployment procedures
- API modifications

---

## Regulatory Compliance

Ensure all contributions:

- Comply with TCPA regulations
- Respect privacy laws (GDPR, CCPA)
- Follow telemarketing guidelines
- Include proper consent mechanisms
- Maintain audit logs

---

## Communication

- Open issues for bug reports
- Use pull requests for features
- Join discussions for questions

---

Thank you for contributing to voice AI automation!