%define		plugin	flake8
Summary:	Vim plugin: flake8
Name:		vim-plugin-%{plugin}
Version:	1.7
Release:	1
License:	Vim
Group:		Applications/Editors/Vim
Source0:	https://github.com/nvie/vim-flake8/archive/%{version}.tar.gz
# Source0-md5:	080d1614fbf41e5b7fb24c29d9858085
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

install -d $RPM_BUILD_ROOT%{_vimdatadir}/{autoload,ftplugin}
cp -a autoload/*.vim $RPM_BUILD_ROOT%{_vimdatadir}/autoload
cp -a ftplugin/*.vim $RPM_BUILD_ROOT%{_vimdatadir}/ftplugin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.mdown
%{_vimdatadir}/autoload/flake8.vim
%{_vimdatadir}/ftplugin/python_flake8.vim
