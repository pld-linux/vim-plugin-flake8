%define		plugin	flake8
Summary:	Vim plugin: flake8
Name:		vim-plugin-%{plugin}
Version:	1.4
Release:	1
License:	Vim
Group:		Applications/Editors/Vim
Source0:	https://github.com/nvie/vim-flake8/archive/%{version}.tar.gz
# Source0-md5:	ed3029ccf91d677129a84f5ad924cc33
URL:		https://github.com/nvie/vim-flake8
Requires:	flake8
Requires:	vim-rt >= 4:7.2.170
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
Vim plugin that runs the currently open file through Flake8, a static
syntax and style checker for Python source code.

%prep
%setup -q -n vim-%{plugin}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}/ftplugin
cp -a */*.vim $RPM_BUILD_ROOT%{_vimdatadir}/ftplugin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.mdown
%{_vimdatadir}/ftplugin/python_flake8.vim
