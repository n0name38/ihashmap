Name:           ihashmap
Version:        1.0.5
Release:        1%{?dist}
Summary:        Indexed hashmap wrapper in Python

Group:          $REPO_GROUP
License:        MIT
URL:            $REPO_URL
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python3-devel

%description
Automaticly indexed hashmap for quick search and wrapper for things that don't expose .keys method

%prep
%setup -q

%build
%pyproject_wheel

%install
%pyproject_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{python3_sitelib}/ihashmap/
