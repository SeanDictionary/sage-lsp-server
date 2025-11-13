# sage-lsp-server

## [1.0.0] - 2025-11-13

### Added

- Initial release of SageMath LSP Server, a fork of Python LSP Server customized for SageMath syntax and constructs.
- Support for Sage-specific syntax sugar such as `^^` and `R.<x,y> = ...`.
- New linter to check for Sage-specific grammar.
- Formatters adapted for Sage syntax sugar.
- Support hover and signature help for Sage-specific constructs.