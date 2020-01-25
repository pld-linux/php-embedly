%define		plugin embedly
%define		php_min_version 5.0.0
Summary:	Embed.ly PHP API
Name:		php-%{plugin}
Version:	0.3.0
Release:	3
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/embedly/embedly-php/tarball/v0.3.0#/%{plugin}-%{version}.tgz
# Source0-md5:	75b94414ec5967bcb226325e888745bb
Patch0:		php52.patch
URL:		http://embed.ly/docs
BuildRequires:	/usr/bin/php
BuildRequires:	rpmbuild(macros) > 1.268
Requires:	php(core) >= %{php_min_version}
Requires:	php(curl)
Requires:	php(json)
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{php_data_dir}

%description
Embedly is the best way to retrieve meta data associated with a URL.
We offer a full suite of tools that you can tailor to your needs to
make embedding simple and easy. These docs will help you understand
how to get the most out of Embedly and how the API works. If you are
new to Embedly we suggest reading the Getting Stared tutorial. It will
give you a basic idea of how Embedly works and its benefits.

%prep
%setup -qc
mv embedly-embedly-php-*/* .
%patch0 -p1

%build
php -l src/Embedly/Embedly.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_data_dir}/Embedly,%{_examplesdir}/%{name}-%{version}}
cp -p src/Embedly/Embedly.php $RPM_BUILD_ROOT%{php_data_dir}/Embedly

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst MIT-LICENSE
%{php_data_dir}/Embedly
%{_examplesdir}/%{name}-%{version}
